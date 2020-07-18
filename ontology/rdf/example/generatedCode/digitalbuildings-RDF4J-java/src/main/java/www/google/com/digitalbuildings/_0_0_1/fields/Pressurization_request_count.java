package www.google.com.digitalbuildings._0_0_1.fields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.subfields.IRequest;
import www.google.com.digitalbuildings._0_0_1.subfields.Request;
import www.google.com.digitalbuildings._0_0_1.subfields.ICount;
import www.google.com.digitalbuildings._0_0_1.subfields.Count;
import www.google.com.digitalbuildings._0_0_1.subfields.IPressurization;
import www.google.com.digitalbuildings._0_0_1.subfields.Pressurization;


@SuppressWarnings("serial")
public class Pressurization_request_count extends www.google.com.digitalbuildings._0_0_1.fields.Field implements IPressurization_request_count{

	IRI newInstance;
	public Pressurization_request_count(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/fields#Pressurization_request_count"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addComposedOfCount (ICount parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<ICount> getComposedOfCount (){
		Set<ICount> ComposedOfCount = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Count) {
				ComposedOfCount.add((Count)action);
			}
		});
		return ComposedOfCount;
	}


  public void addComposedOfPressurization (IPressurization parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<IPressurization> getComposedOfPressurization (){
		Set<IPressurization> ComposedOfPressurization = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Pressurization) {
				ComposedOfPressurization.add((Pressurization)action);
			}
		});
		return ComposedOfPressurization;
	}


  public void addComposedOfRequest (IRequest parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<IRequest> getComposedOfRequest (){
		Set<IRequest> ComposedOfRequest = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Request) {
				ComposedOfRequest.add((Request)action);
			}
		});
		return ComposedOfRequest;
	}

	public static Set<IPressurization_request_count> getAllPressurization_request_countsObjectsCreated(){
		Set<IPressurization_request_count> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/fields#Pressurization_request_count")).subjects().stream()
		.map(mapper->(IPressurization_request_count)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}