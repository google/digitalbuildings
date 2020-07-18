package www.google.com.digitalbuildings._0_0_1.fields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.subfields.ICapacity;
import www.google.com.digitalbuildings._0_0_1.subfields.Capacity;
import www.google.com.digitalbuildings._0_0_1.subfields.IPower;
import www.google.com.digitalbuildings._0_0_1.subfields.Power;


@SuppressWarnings("serial")
public class Power_capacity extends www.google.com.digitalbuildings._0_0_1.fields.Field implements IPower_capacity{

	IRI newInstance;
	public Power_capacity(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/fields#Power_capacity"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addComposedOfCapacity (ICapacity parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<ICapacity> getComposedOfCapacity (){
		Set<ICapacity> ComposedOfCapacity = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Capacity) {
				ComposedOfCapacity.add((Capacity)action);
			}
		});
		return ComposedOfCapacity;
	}


  public void addComposedOfPower (IPower parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<IPower> getComposedOfPower (){
		Set<IPower> ComposedOfPower = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Power) {
				ComposedOfPower.add((Power)action);
			}
		});
		return ComposedOfPower;
	}

	public static Set<IPower_capacity> getAllPower_capacitysObjectsCreated(){
		Set<IPower_capacity> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/fields#Power_capacity")).subjects().stream()
		.map(mapper->(IPower_capacity)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}