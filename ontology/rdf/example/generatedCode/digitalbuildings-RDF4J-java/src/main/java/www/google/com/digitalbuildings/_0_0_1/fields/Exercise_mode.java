package www.google.com.digitalbuildings._0_0_1.fields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.subfields.IExercise;
import www.google.com.digitalbuildings._0_0_1.subfields.Exercise;
import www.google.com.digitalbuildings._0_0_1.subfields.IMode;
import www.google.com.digitalbuildings._0_0_1.subfields.Mode;


@SuppressWarnings("serial")
public class Exercise_mode extends www.google.com.digitalbuildings._0_0_1.fields.Field implements IExercise_mode{

	IRI newInstance;
	public Exercise_mode(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/fields#Exercise_mode"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addComposedOfExercise (IExercise parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<IExercise> getComposedOfExercise (){
		Set<IExercise> ComposedOfExercise = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Exercise) {
				ComposedOfExercise.add((Exercise)action);
			}
		});
		return ComposedOfExercise;
	}


  public void addComposedOfMode (IMode parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<IMode> getComposedOfMode (){
		Set<IMode> ComposedOfMode = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Mode) {
				ComposedOfMode.add((Mode)action);
			}
		});
		return ComposedOfMode;
	}

	public static Set<IExercise_mode> getAllExercise_modesObjectsCreated(){
		Set<IExercise_mode> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/fields#Exercise_mode")).subjects().stream()
		.map(mapper->(IExercise_mode)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}