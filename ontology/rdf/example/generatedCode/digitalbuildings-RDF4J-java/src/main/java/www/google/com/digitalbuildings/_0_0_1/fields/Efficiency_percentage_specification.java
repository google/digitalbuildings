package www.google.com.digitalbuildings._0_0_1.fields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.subfields.IEfficiency;
import www.google.com.digitalbuildings._0_0_1.subfields.Efficiency;
import www.google.com.digitalbuildings._0_0_1.subfields.IPercentage;
import www.google.com.digitalbuildings._0_0_1.subfields.Percentage;
import www.google.com.digitalbuildings._0_0_1.subfields.ISpecification;
import www.google.com.digitalbuildings._0_0_1.subfields.Specification;


@SuppressWarnings("serial")
public class Efficiency_percentage_specification extends www.google.com.digitalbuildings._0_0_1.fields.Field implements IEfficiency_percentage_specification{

	IRI newInstance;
	public Efficiency_percentage_specification(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/fields#Efficiency_percentage_specification"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addComposedOfEfficiency (IEfficiency parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<IEfficiency> getComposedOfEfficiency (){
		Set<IEfficiency> ComposedOfEfficiency = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Efficiency) {
				ComposedOfEfficiency.add((Efficiency)action);
			}
		});
		return ComposedOfEfficiency;
	}


  public void addComposedOfPercentage (IPercentage parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<IPercentage> getComposedOfPercentage (){
		Set<IPercentage> ComposedOfPercentage = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Percentage) {
				ComposedOfPercentage.add((Percentage)action);
			}
		});
		return ComposedOfPercentage;
	}


  public void addComposedOfSpecification (ISpecification parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<ISpecification> getComposedOfSpecification (){
		Set<ISpecification> ComposedOfSpecification = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Specification) {
				ComposedOfSpecification.add((Specification)action);
			}
		});
		return ComposedOfSpecification;
	}

	public static Set<IEfficiency_percentage_specification> getAllEfficiency_percentage_specificationsObjectsCreated(){
		Set<IEfficiency_percentage_specification> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/fields#Efficiency_percentage_specification")).subjects().stream()
		.map(mapper->(IEfficiency_percentage_specification)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}